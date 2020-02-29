from pyhive import hive

host_name = "192.168.56.101"
port = 8888
user = "cloudera"
password = "cloudera"
database="aa_hsh"

def hiveconnection(host_name, port, user,password, database):
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('select * from auth limit 50')
    result = cur.fetchall()

    return result

# Call above function
output = hiveconnection(host_name, port, user,password, database)
print(output)