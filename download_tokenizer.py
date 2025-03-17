import os
import json
from transformers import GPT2TokenizerFast

def setup_tokenizer():
    cache_dir = os.path.join("J:", "MaxKB", "data", "model", "tokenizer", "gpt2")
    os.makedirs(cache_dir, exist_ok=True)
    
    # 基本配置
    config = {
        "tokenizer_class": "GPT2TokenizerFast",
        "model_max_length": 1024,
        "padding_side": "right",
        "truncation_side": "right",
        "add_prefix_space": False
    }
    
    # 保存配置文件
    config_path = os.path.join(cache_dir, "tokenizer_config.json")
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    
    # 创建基本的词汇表和合并规则文件
    vocab_path = os.path.join(cache_dir, "vocab.json")
    merges_path = os.path.join(cache_dir, "merges.txt")
    
    if not os.path.exists(vocab_path):
        # 创建一个基本的词汇表
        vocab = {"<|endoftext|>": 0}
        with open(vocab_path, 'w', encoding='utf-8') as f:
            json.dump(vocab, f, indent=2)
    
    if not os.path.exists(merges_path):
        # 创建一个空的合并规则文件
        with open(merges_path, 'w', encoding='utf-8') as f:
            f.write("")
    
    try:
        # 尝试初始化分词器
        tokenizer = GPT2TokenizerFast(
            vocab_file=vocab_path,
            merges_file=merges_path,
            tokenizer_file=None
        )
        print("分词器设置成功！")
        
        # 测试分词器
        test_text = "这是一个测试文本"
        tokens = tokenizer.tokenize(test_text)
        print(f"测试文本分词结果: {tokens}")
        
    except Exception as e:
        print(f"设置分词器时出错: {str(e)}")

if __name__ == "__main__":
    setup_tokenizer() 