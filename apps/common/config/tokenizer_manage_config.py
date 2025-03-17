# coding=utf-8
"""
    @project: maxkb
    @Author：虎
    @file： tokenizer_manage_config.py
    @date：2024/4/28 10:17
    @desc:
"""


class TokenizerManage:
    tokenizer = None

    @staticmethod
    def get_tokenizer():
        from transformers import GPT2TokenizerFast
        import os
        import json
        
        if TokenizerManage.tokenizer is None:
            cache_dir = os.path.join("J:", "MaxKB", "data", "model", "tokenizer", "gpt2")
            os.makedirs(cache_dir, exist_ok=True)
            
            # 检查必要的文件是否存在
            required_files = {
                "tokenizer_config.json": {
                    "content": {
                        "tokenizer_class": "GPT2TokenizerFast",
                        "model_max_length": 1024,
                        "padding_side": "right",
                        "truncation_side": "right",
                        "add_prefix_space": False
                    }
                },
                "vocab.json": None,
                "merges.txt": None
            }
            
            # 创建必要的配置文件
            for filename, config in required_files.items():
                file_path = os.path.join(cache_dir, filename)
                if not os.path.exists(file_path):
                    if config and filename.endswith('.json'):
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(config["content"], f, indent=2)
                    else:
                        # 如果文件不存在，创建空文件
                        open(file_path, 'a').close()
            
            try:
                TokenizerManage.tokenizer = GPT2TokenizerFast(
                    vocab_file=os.path.join(cache_dir, "vocab.json"),
                    merges_file=os.path.join(cache_dir, "merges.txt"),
                    tokenizer_file=None
                )
            except Exception as e:
                print(f"加载本地分词器失败: {str(e)}")
                # 如果本地加载失败，使用默认的空白分词器
                TokenizerManage.tokenizer = GPT2TokenizerFast.from_pretrained("gpt2", local_files_only=True)
                
        return TokenizerManage.tokenizer
