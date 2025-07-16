from ping3 import ping
import socket

def ping_host(ip):
    response = ping(ip, timeout=1)
    return response is not None
    
def scan_port(ip, port):
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.settimeout(2)
     
     try:
          s.connect((ip, port))
          s.close()
          return True
     except:
          return False

def scan_ports(ip):
     porte_da_controllare= [22, 80, 443, 3389, 8080]
     porte_aperte = []

     for port in porte_da_controllare:
          print(f" Controllo {ip}:{port}")
          if scan_port(ip, port):
               print(f" Porta {port} APERTA")
               porte_aperte.append(port)
          else:
               print(f" Porta {port} CHIUSA o non raggiungibile")
    
     return porte_aperte

def main():

    for i in range (1,6):

        ip = (f"192.168.1.{i}")
        print(f"\n Scansione IP: {ip}...")
        
        if ping_host(ip): 

                print(f"ok! Host attivo: {ip}")
                porte = scan_ports(ip)
                print(f" Porte aperte su {ip}: {porte if porte else 'nessuna'}")
        else:
                print(f"Nessuna risposta da: {ip}")


if __name__=="__main__":
    main()
