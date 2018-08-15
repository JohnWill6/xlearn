#include "src/loss/embed.h"

namespace xLearn {

void embed_thread(const DMatrix* matrix,
                 Model* model,
                 std::vector<std::string>* ins,
                 Score* score_func_,
                 bool is_norm,
                 size_t start_idx,
                 size_t end_idx) {
  CHECK_GE(end_idx, start_idx);
  for (size_t i = start_idx; i < end_idx; ++i) {
    SparseRow* row = matrix->row[i];
    real_t norm = is_norm ? matrix->norm[i] : 1.0;
    real_t y = matrix->Y[i];
    (*ins)[i] = score_func_->FeaTransform(row, *model, y, norm);
  }
}

void Embed::FeaTransform(const DMatrix* matrix,
                         Model& model,
                         std::vector<std::string>& ins) {
  CHECK_NOTNULL(matrix);
  CHECK_NE(ins.empty(), true);
  CHECK_EQ(ins.size(), matrix->row_length);
  index_t row_len = matrix->row_length;
  // Predict in multi-thread
  for (int i = 0; i < threadNumber_; ++i) {
    size_t start_idx = getStart(row_len, threadNumber_, i);
    size_t end_idx = getEnd(row_len, threadNumber_, i);
    pool_->enqueue(std::bind(embed_thread,
                             matrix,
                             &model,
                             &ins,
                             score_func_,
                             norm_,
                             start_idx,
                             end_idx));
  }
  // Wait all of the threads finish their job
  pool_->Sync(threadNumber_);
}

}  // namespace xLearn
