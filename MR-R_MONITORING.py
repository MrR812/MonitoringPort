import psutil
import time

def get_connected_ips_on_port(port):
    connected_ips = set()
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED' and conn.laddr.port == port:
            connected_ips.add(conn.raddr.ip)
    return connected_ips

def main():
    port = 30120 #PORT YANG INGIN DIMONITORING
    while True:
        connected_ips = get_connected_ips_on_port(port)
        print(f"IP yang terhubung ke port {port}:")
        for ip in connected_ips:
            print(ip)
        time.sleep(5)  # Tunggu 5 detik sebelum mengulang loop

if __name__ == "__main__":
    main()