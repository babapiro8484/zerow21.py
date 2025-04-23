import requests

API_URL = "https://41fe423b-06a1-4435-9ead-ec01085d7126-00-3ogsrh5i5qbha.sisko.replit.dev/"

def login_check(username, password):
    try:
        response = requests.post(f"{API_URL}/login", json={
            "username": username,
            "password": password
        })
        result = response.json()
        return result
    except:
        return {"status": False, "message": "Servera bağlanılamadı"}

username = input("Kullanıcı adı: ")
password = input("Şifre: ")

login_result = login_check(username, password)

if login_result["status"]:
    if login_result["role"] == "admin":
        print("Hoşgeldin admin! Tüm özelliklere erişimin var.")
        # buraya admin fonksiyonları çağırılır
    elif login_result["role"] == "user":
        print("Hoşgeldin kullanıcı.")
        # buraya user fonksiyonları çağırılır
else:
    print("Giriş başarısız:", login_result["message"])
    exit()

# Current version of the script 
debug_mode = False
CURRENT_VERSION = """
2.6.10
"""
CURRENT_VERSION=CURRENT_VERSION.replace('\n','')
server_online = "https://7eab950d-c959-4bf9-afdf-f0bf12b31b4c-00-2lxn7evq463k.sisko.replit.dev"
mode_server = server_online
"""
-------------------------------------------
MAJOR (Angka Pertama):

Angka ini meningkat ketika ada perubahan yang tidak kompatibel yang mengharuskan 
pengguna untuk memodifikasi kode atau penggunaan mereka yang ada. Misalnya, 
jika suatu fungsi dihapus atau perilakunya berubah secara signifikan, Anda akan 
meningkatkan versi mayor.
-------------------------------------------
MINOR (Angka Kedua):

Angka ini meningkat ketika fitur baru ditambahkan dengan cara yang kompatibel 
dengan versi sebelumnya. Ini berarti bahwa fungsionalitas yang ada tetap tidak 
berubah, tetapi kemampuan atau peningkatan baru diperkenalkan. Misalnya, 
jika fungsi baru ditambahkan tanpa memengaruhi yang sudah ada, Anda akan 
menaikkan versi minor.
-------------------------------------------
PATCH (Angka Ketiga):

Angka ini meningkat ketika perbaikan bug yang kompatibel dengan versi sebelumnya 
diperkenalkan. Ini biasanya merupakan perubahan kecil yang menyelesaikan masalah 
tanpa menambah fitur baru atau merusak fungsionalitas yang ada. Misalnya, 
jika ada bug yang diperbaiki dalam suatu fungsi tetapi antarmuka fungsi tersebut 
tetap sama, Anda akan menaikkan versi patch.
-------------------------------------------
"""



import os,sys,random,requests


VERSION_CHECK_URL = f"{mode_server}/termux-version"

def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        # Pastikan direktori ada
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")
        
def update_script():
    version_info = get_latest_version_info()
    if not version_info:
        return
    
    latest_version = version_info.get("version")
    download_url = version_info.get("download_url")
    print(download_url)
    print(f"CURRENT_VERSION {CURRENT_VERSION}\nlatest_version {latest_version}\ndownload_url {download_url}")
    if latest_version and download_url:
        if latest_version != CURRENT_VERSION:
            print(f"New version available: {latest_version}")
            print(f"Downloading update... {download_url}")
            download_new_version(download_url, sys.argv[0])
            print("Script updated to the latest version. Please restart the script.")
            exit()
        else:
            print("You already have the latest version.")
    else:
        print("Invalid version information received.")
update_script()


import platform
from datetime import datetime
local_ip = requests.get('https://api.ipify.org').text
response = requests.get(f"https://ipinfo.io/{local_ip}/json")
data_jaringan = response.json()

try:
    from colorama import init, Fore, Back, Style
    init()
    # Fungsi color pengganti menggunakan colorama
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = requests.get('https://api.ipify.org').text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    
    # Reinisialisasi setelah install
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem



def disp(clrnama):
    def get_closest_color(r, g, b):
        # Memetakan warna RGB ke warna colorama terdekat
        colors = {
            'RED': (255, 0, 0, Fore.RED),
            'GREEN': (0, 255, 0, Fore.GREEN),
            'BLUE': (0, 0, 255, Fore.BLUE),
            'YELLOW': (255, 255, 0, Fore.YELLOW),
            'MAGENTA': (255, 0, 255, Fore.MAGENTA),
            'CYAN': (0, 255, 255, Fore.CYAN),
            'WHITE': (255, 255, 255, Fore.WHITE)
        }
        
        min_distance = float('inf')
        closest_color = Fore.WHITE  # default
        
        for _, (cr, cg, cb, color) in colors.items():
            distance = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
            if distance < min_distance:
                min_distance = distance
                closest_color = color
                
        return closest_color

    clrfirsttime = True
    clrVnama = clrnama.split("[")
    clrdisps = clrVnama[0]
    
    for clrx in clrVnama:
        if clrfirsttime == False:
            try:
                # Mengkonversi hex ke RGB
                clrcode1 = int(clrx[0:2], 16)
                clrcode2 = int(clrx[2:4], 16)
                clrcode3 = int(clrx[4:6], 16)
                clrhuruf = clrx[7:8]
                
                # Mendapatkan warna colorama terdekat
                closest_color = get_closest_color(clrcode1, clrcode2, clrcode3)
                clrdisps += closest_color + clrhuruf + Style.RESET_ALL
            except:
                clrdisps += clrx[7:8]
                
        if clrfirsttime:
            clrfirsttime = False

    clrdisps += clrVnama[len(clrVnama)-1][8:len(clrVnama[len(clrVnama)-1])]
    return clrdisps

warnasekarang=""
def generate(namax):
    global warnasekarang
    gabungwarna = ""
    contohnama = namax
    # proses memecah huruf di nama
    data = {
        "huruf": "",
        "kodewarna": [255, 0, 0],
        "mode": 1,
        "kodewarnaCPM": ""
    }
    while True:
        while True:
            tanya = random.choice(["merah","kuning","hijau","biru","ungu","pink"])
            if tanya!=warnasekarang:
                warnasekarang = tanya
                break
        if tanya == "merah":
            data["kodewarna"] = [255, 0, 0]
            break
        elif tanya == "kuning":
            data["kodewarna"] = [230, 245, 66]
            break
        elif tanya == "hijau":
            data["kodewarna"] = [0, 255, 0]
            break
        elif tanya == "biru":
            data["kodewarna"] = [0, 0, 255]
            break
        elif tanya == "ungu":
            data["kodewarna"] = [150, 66, 245]
            break
        elif tanya == "pink":
            data["kodewarna"] = [245, 66, 215]
            break
        else:
            print("Harus sesuai pilihan warna ..!")

    for huruf in contohnama:
        while True:
            # print(f"\nmode sekarang : {data['mode']}")
            tambah = 45
            if data["mode"] == 1:
                if data["kodewarna"][1]+tambah <= 255:
                    data["kodewarna"][1] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 255, 0]
            elif data["mode"] == 2:
                if data["kodewarna"][0]-tambah >= 0:
                    data["kodewarna"][0] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 0]
            elif data["mode"] == 3:
                if data["kodewarna"][2]+tambah >= 255:
                    data["kodewarna"][2] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 255]
            elif data["mode"] == 4:
                if data["kodewarna"][1]-tambah >= 0:
                    data["kodewarna"][1] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 0, 255]
            elif data["mode"] == 5:
                if data["kodewarna"][0]+tambah >= 255:
                    data["kodewarna"][0] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 0, 255]
            elif data["mode"] == 6:
                if data["kodewarna"][2]-tambah >= 255:
                    data["kodewarna"][2] -= tambah
                    break
                else:
                    data["mode"] = 1
                    data["kodewarna"] = [255, 0, 0]
        # print(f"{huruf} {data['kodewarna']}")
        gabungwarna += color(huruf,
                             fore=(data["kodewarna"][0],
                                   data["kodewarna"][1],
                                   data["kodewarna"][2]),
                             back=(0, 0, 0))
        kodas = []
        for t in range(3):
            clrcode = hex(data["kodewarna"][t])[2::]
            if len(clrcode) == 1:
                clrcode += "0"
            kodas.append(clrcode)
        data["kodewarnaCPM"] += f"[{kodas[0]}{kodas[1]}{kodas[2]}]{huruf}"
    # print(f"hasil\t:  {disp(data['kodewarnaCPM'])}")
    # print(f"kode\t:  {data['kodewarnaCPM']}")
    return data["kodewarnaCPM"]
def refresh_x():
    import inspect
    kucing_garong = inspect.getfile(inspect.currentframe())
    with open(kucing_garong, 'r') as file:
        gajah_terbang = file.read()
        gajah_duduk = len(gajah_terbang)
    return gajah_duduk
pySystem.Clear()
pySystem.Size(80, 40)


text = """
< [ TİKTOK:zerow.cp] > X < [ https://41fe423b-06a1-4435-9ead-ec01085d7126-00-3ogsrh5i5qbha.sisko.replit.dev/ ] >"""[1:]

banner = r"""

  ███████╗███████╗██████╗  ██████╗ ██╗    ██╗
  ██╔════╝██╔════╝██╔══██╗██╔═══██╗██║    ██║
  █████╗  █████╗  ██████╔╝██║   ██║██║ █╗ ██║
  ██╔══╝  ██╔══╝  ██╔═══╝ ██║   ██║██║███╗██║
  ███████╗███████╗██║     ╚██████╔╝╚███╔███╔╝
  ╚══════╝╚══════╝╚═╝      ╚═════╝  ╚══╝╚═
pyAnime.Fade(pyCenter.Center(banner), pyColors.purple_to_red, pyColorate.Vertical, enter=True)

pySystem.Clear()

print("\n"*2    )
print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
print("\n"*2)


delet=["cpm/pos.py","cpm/__init__.py"]
for psdd in delet:
    if os.path.exists(f"{psdd}") == True:
        os.system(f"rm {psdd}")



def c(colr, tex):
    try:
        w = {
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "CYAN": Fore.CYAN,
            "YELLOW": Fore.YELLOW,
            "GOLD": Fore.YELLOW  # Colorama tidak memiliki gold, gunakan yellow sebagai alternatif
        }
        return w[colr.upper()] + tex + Style.RESET_ALL
    except:
        return tex
def mask_password(password):
    if len(password) <= 3:
        return password
    return password[:3] + '*' * (len(password) - 3)
def heder():
        if Your_Data['username']:
            get_userInfo()
        pySystem.Clear()
        print(f"build : {refresh_x()}")
        versi_tampil = disp(generate(f"Topix SB CPM TOOLS {CURRENT_VERSION}"))
        loc_info = f"  Location\t  : {data_jaringan.get('city')}, {data_jaringan.get('region')}, {data_jaringan.get('country')}"
        loc_info = pyColorate.Horizontal(pyColors.green_to_yellow, loc_info)
        isp_info = f"  ISP     \t  : {data_jaringan.get('org')}"
        isp_info = pyColorate.Horizontal(pyColors.green_to_yellow, isp_info)
        bannerwz = f"""{c("cyan","=====================================================")}
  {versi_tampil} {c("cyan","||")} {c("green","https://account.topixsb.dev/")}
{c("cyan","=====================================================")}
{loc_info}
{isp_info}"""
        if Your_Data['email_web']:
            data_client=f"""
  username   : {Your_Data['username']}
  role       : {Your_Data['role']}
  money      : {Your_Data['∞']}
  expire_at  : {Your_Data['expire_at']}
  last login : {Your_Data['last_login_date']}"""
            if 'email' in Your_Data:
                data_client+=f"""\n\n  Car Parking Email : {Your_Data["email"]}
  Car Parking Passw : {mask_password(Your_Data["password"])}"""
            
            bannerwz+=pyColorate.Horizontal(pyColors.green_to_yellow, data_client)
        print(bannerwz)

tex="""     IMPORTANT READ

    You must log out of the CPM application first, 
    unless you only want to use the "Inject Rank" and "Instant Rank" features, 
    as these two features do not require you to log out.

    Please refill your cash only at https://account.topixsb.dev

"""

print(pyColorate.Horizontal(pyColors.green_to_yellow, pyCenter.XCenter(tex)))



def warnain(text,inpo="",title=""):
    tex = f"""{c("cyan","=====================================================")}"""
    if inpo:
        tex+=f"\n\t\t{pyColorate.Horizontal(pyColors.red_to_purple, inpo)}"
    if title:
        tex+=f"\n\t\t{pyColorate.Horizontal(pyColors.cyan_to_green, title)}"
    tex+=f"""
{pyColorate.Horizontal(pyColors.cyan_to_green, text)}
{c("cyan","=====================================================")}"""
    print(tex)


def send_registration_data(uname, upass):
    url = f"{mode_server}/register-acc"
    
    data = {
        "username": uname,
        "password": upass
    }
    
    try:
        response = requests.post(url, data=data)
        
        # Pastikan untuk memanggil .json() untuk mendapatkan data JSON
        response_data = response.json()
        return response_data
    except Exception as e:
        return f"An error occurred: {e}"
def send_login_data(uname, upass):
    url = f"{mode_server}/login-acc"
    
    data = {
        "username": uname,
        "password": upass
    }
    
    try:
        response = requests.post(url, data=data)
        
        if debug_mode:
            print(f"Response status: {response.status_code}")
            print(f"Response text: {response.text}")
        
        if response.status_code != 200:
            try:
                error_data = response.json()
                return {
                    "status": False, 
                    "message": error_data.get('message', 'Unknown error occurred')
                }
            except:
                return {
                    "status": False, 
                    "message": f"Server error: {response.status_code}"
                }
            
        try:
            response_data = response.json()
            
            if response_data['status']:
                # Simpan semua data user termasuk token
                Your_Data.update({
                    'access_token': response_data['access_token'],
                    'username': response_data['data']['username'],
                    'role': response_data['data']['role'],
                    'money': response_data['data']['money'],
                    'email_web': response_data['data']['email'],
                    'last_login': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Tambahkan waktu login
                })
            return response_data
            
        except ValueError as e:
            return {
                "status": False, 
                "message": f"Invalid JSON response: {response.text}"
            }
            
    except requests.RequestException as e:
        return {
            "status": False, 
            "message": f"Request error: {str(e)}"
        }
    except Exception as e:
        return {
            "status": False, 
            "message": f"Unexpected error: {str(e)}"
        }

def serper(cit, datanya):
    # Cek apakah token masih ada
    if not Your_Data.get('access_token'):
        return {"status": False, "message": "Silakan login terlebih dahulu"}

    url = f"{mode_server}/app_endpoint"

    data = {
        "access_token": Your_Data['access_token'],
        "username": Your_Data['username'],
        "item": {
            "name": cit
        },
        "email": Your_Data.get('email', ''),
        "password": Your_Data.get('password', '')
    }
    
    for x in datanya:
        data[x] = datanya[x]
        
    try:
        response = requests.post(url, json=data)
        
        # Handle berbagai status code
        if response.status_code == 401:
            # Token expired atau invalid
            Your_Data.clear()
            Your_Data.update({
                'email_web': None, 
                'expire_at': None, 
                'last_login_date': None, 
                'money': None, 
                'role': None, 
                'username': None,
                'access_token': None
            })
            return {"status": False, "message": "Sesi anda telah berakhir, silakan login kembali"}
        elif response.status_code == 429:
            # Rate limit
            return {"status": False, "message": "Terlalu banyak request, mohon tunggu beberapa saat"}
        elif response.status_code >= 500:
            # Server error
            return {"status": False, "message": "Server sedang bermasalah, coba lagi nanti"}
            
        try:
            result = response.json()
            return result
        except ValueError:
            return {"status": False, "message": f"Invalid JSON re
