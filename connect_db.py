import sys
import boto3

ssm = boto3.client("ssm")


def get_ssm_secret(parameter_name):
    return ssm.get_parameter(
        Name="/Prod/Db/Password",
        WithDecryption=True
    )


if __name__ == "__main__":
    name = sys.argv[1]

    secret = get_ssm_secret(name)

    password = secret.get("Parameter").get("Value")

    conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db="/Prod/Db/Password")
						   
						   
	print(dir(conn))
	
	with conn:
        cur = connection.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        print("Database version: {} ".format(version[0]))
