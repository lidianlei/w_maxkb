import os
import sys
import time
from sentence_transformers import SentenceTransformer
import torch

# 设置模型缓存目录
cache_dir = "J:/MaxKB/data/model/cache"
os.makedirs(cache_dir, exist_ok=True)

# 设置 huggingface 缓存目录
os.environ['TRANSFORMERS_CACHE'] = cache_dir
os.environ['HF_HOME'] = cache_dir

def download_model(retries=3):
    for attempt in range(retries):
        try:
            print(f"开始下载模型... (尝试 {attempt + 1}/{retries})")
            model = SentenceTransformer('shibing624/text2vec-base-chinese', 
                                      cache_folder=cache_dir,
                                      device="cpu")
            
            # 测试模型是否正常工作
            test_text = "测试文本"
            embeddings = model.encode(test_text)
            print(f"模型测试成功，维度: {len(embeddings)}")
            print(f"模型已成功下载到: {cache_dir}")
            return True
        except Exception as e:
            print(f"尝试 {attempt + 1} 失败: {str(e)}")
            if attempt < retries - 1:
                print("等待5秒后重试...")
                time.sleep(5)
            else:
                print("所有尝试都失败了。")
                return False

if __name__ == "__main__":
    success = download_model()
    if not success:
        sys.exit(1)