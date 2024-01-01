from urllib.parse import quote_plus


username = "manjinder_singh"
password = "Engineering96@"
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)
MONGO_DB_URL = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.ftk5qa5.mongodb.net/?retryWrites=true&w=majority"


MONGODB_URL_KEY = MONGO_DB_URL
# AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
# AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
# REGION_NAME = "us-east-1"

