-- 1. 首先，添加新的 asker_id 列
ALTER TABLE application_chat ADD COLUMN asker_id uuid;

-- 2. 从 application 表获取用户 ID 并更新 asker_id
UPDATE application_chat 
SET asker_id = application.user_id 
FROM application 
WHERE application_chat.application_id = application.id;

-- 3. 删除旧的 asker 列
ALTER TABLE application_chat DROP COLUMN asker;

-- 4. 添加外键约束
ALTER TABLE application_chat 
ADD CONSTRAINT application_chat_asker_id_fk 
FOREIGN KEY (asker_id) 
REFERENCES users_user(id) 
ON DELETE DO NOTHING; 