from dotenv import load_dotenv

load_dotenv()

host = 
port = os.getenv("DB_PORT")
name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

username = os.getenv("USER_ORADB")
password = os.getenv("PASS_ORADB")
dsn = os.getenv("HOST_ORADB")
port = os.getenv("PORT_ORADB")
encoding = os.getenv("ENCODING_ORADB")
database=os.getenv("DATABASE_ORADB")

hostMysql = os.getenv("HOST_MYSQL")
userMysql = os.getenv("USER_MYSQL")
passMysql = os.getenv("PASS_MYSQL")
portMysql = os.getenv("PASS_MYSQL")
dbMysql = os.getenv("DB_MYSQL")
