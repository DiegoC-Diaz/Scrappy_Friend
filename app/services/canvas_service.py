from canvasapi import Canvas

def get_files():
    # Logic to get files from Canvas
    
    return [{"file_name": "file1.pdf"}]

def get_tasks():
    # Logic to get tasks from Canvas
    return [{"task_name": "task1"}]

def get_scores():
    # Logic to get scores from Canvas
    return [{"score": 95}]

def get_authorization(api_key,api_url):
    canvas = Canvas(api_url, api_key)
    user = canvas.get_user(1)
    


    return {"status":True}