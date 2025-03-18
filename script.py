import argparse
import requests
import time
import threading
import multiprocessing
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PhotoFetcher:
    def __init__(self, mode, limit):
        self.mode = mode
        self.limit = limit
    
    def obtener_fotos(self):
        url = "https://jsonplaceholder.typicode.com/photos"
        response = requests.get(url)
        if response.status_code == 200:
            fotos = response.json()
            return fotos[:self.limit] if self.limit else fotos
        else:
            logging.error("Error al obtener fotos")
            return []

    def obtener_album(self, album_id):
        url = f"https://jsonplaceholder.typicode.com/albums/{album_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error al obtener el álbum {album_id}")
            return None

    def procesar_foto(self, foto):
        album = self.obtener_album(foto['albumId'])
        if album:
            print(f"Foto ID: {foto['id']}\nTítulo: {foto['title']}\nURL: {foto['url']}\nÁlbum ID: {album['id']}\nÁlbum Título: {album['title']}\n")

    def modo_secuencial(self, fotos):
        for foto in fotos:
            self.procesar_foto(foto)

    def modo_multihilos(self, fotos):
        hilos = []
        for foto in fotos:
            hilo = threading.Thread(target=self.procesar_foto, args=(foto,))
            hilos.append(hilo)
            hilo.start()
        for hilo in hilos:
            hilo.join()

    def modo_multiprocesos(self, fotos):
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            pool.map(self.procesar_foto, fotos)

    def ejecutar(self):
        inicio = time.time()
        fotos = self.obtener_fotos()
        
        if self.mode == 'secuencial':
            self.modo_secuencial(fotos)
        elif self.mode == 'multihilos':
            self.modo_multihilos(fotos)
        elif self.mode == 'multiprocesos':
            self.modo_multiprocesos(fotos)
        
        fin = time.time()
        print(f"Tiempo total de ejecución: {fin - inicio:.3f} segundos")


def main():
    parser = argparse.ArgumentParser(description='Obtener fotos y álbumes en diferentes modos de ejecución')
    parser.add_argument('--mode', choices=['secuencial', 'multihilos', 'multiprocesos'], required=True, help='Modo de ejecución')
    parser.add_argument('--photos', type=int, help='Cantidad de fotos a obtener (opcional)')
    args = parser.parse_args()
    
    fetcher = PhotoFetcher(args.mode, args.photos)
    fetcher.ejecutar()

if __name__ == '__main__':
    main()
