#ifndef XLEARN_EMBED_H_
#define XLEARN_EMBED_H_

#include <vector>
#include <string>

#include "src/base/common.h"
#include "src/base/math.h"
#include "src/base/thread_pool.h"
#include "src/data/model_parameters.h"
#include "src/score/score_function.h"

namespace xLearn {

class Embed {
 public:
  // Constructor and Desstructor
  Embed()  { }
  ~Embed() { }

  void Initialize(Score* score, 
                  ThreadPool* pool, 
                  bool norm = true,
                  bool lock_free = false,
                  index_t batch_size = 0) {
    CHECK_NOTNULL(score);
    CHECK_NOTNULL(pool);
    CHECK_GE(batch_size, 0);
    score_func_ = score;
    pool_ = pool;
    norm_ = norm;
    threadNumber_ = pool_->ThreadNumber();
    lock_free_ = lock_free;
    batch_size_ = batch_size;
  }

  void FeaTransform(const DMatrix* data_matrix,
                        Model& model,
                        std::vector<std::string>& ins);

 protected:
  /* The score function, including LinearScore,
  FMScore, FFMScore, etc */
  Score* score_func_;
  /* Use instance-wise normalization */
  bool norm_;
  /* Open lock-free training ? */
  bool lock_free_;
  /* Thread pool for multi-thread training */
  ThreadPool* pool_;
  /* Number of thread in thread pool */
  size_t threadNumber_;
  /* Mini-batch size */
  index_t batch_size_;

 private:
  DISALLOW_COPY_AND_ASSIGN(Embed);
};

}  // namespace xLearn

#endif  // XLEARN_EMBED_H_
