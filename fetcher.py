import requests
import time
import csv

def clear_csv():
    with open('db.csv', 'w') as csv_file:
        categories='data,hora,DEI,DEI 5Ghz,EDUROAM,EDUROAM 5Ghz,GUEST,Total\n'
        csv_file.write(categories)


def get_params(lines):
    params = {}
    params['data']=lines[0].split(' ')[0]
    params['hora']=lines[0].split(' ')[1]
    params['DEI']=lines[1].split(': ')[1]
    params['DEI 5Ghz']=lines[2].split(': ')[1]
    params['EDUROAM']=lines[3].split(': ')[1]
    params['EDUROAM 5Ghz']=lines[4].split(': ')[1]
    params['GUEST']=lines[5].split(': ')[1]
    params['Total']=lines[6].split(': ')[1]
    return params

def main():
    while True:
        r = requests.get('http://sic.dei.uc.pt/repo/count_dei_wifi.txt')
        content = str(r.content).replace('\\n', '\n')
        content=content[2:-1]
        print(content)


        with open('db.csv', 'a') as csvfile:
            lines = content.split('\n')
            params = get_params(lines)
            csvfile.write(params['data']+','+params['hora']+','+params['hora']+','+params['DEI']+','+params['DEI 5Ghz']+','+params['EDUROAM']+','+params['EDUROAM 5Ghz']+','+params['GUEST']+','+params['Total']+'\n')

        content += '\n\n\n\n'
        with open("db.txt", 'a') as f:
            f.write(content)


        time.sleep(600)
#clear_csv()
main()



