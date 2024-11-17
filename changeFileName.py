import os

def rename_images_in_folder(folder_path):
    """
    Rinomina tutte le immagini in una cartella con un numero progressivo.
    Ad esempio: 1.jpg, 2.jpg, ecc.
    
    :param folder_path: Percorso della cartella contenente le immagini
    """
    # Estensioni di immagini supportate
    supported_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
    
    try:
        # Ottieni tutti i file nella cartella
        files = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_extensions)]
        
        # Ordina i file per nome (opzionale, utile per un ordine predeterminato)
        files.sort()

        # Rinominare ogni file con un numero progressivo
        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(folder_path, filename)
            new_name = f"{index}.jpg"  # Cambia qui l'estensione predefinita se necessario
            new_path = os.path.join(folder_path, new_name)

            # Rinomina il file
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")

        print("\nRinominazione completata con successo!")
    except Exception as e:
        print(f"Errore: {e}")

# Specifica il percorso della cartella contenente le immagini
folder = r"C:\Users\Davide\Desktop\fotoakira\img"  # Percorso corretto
  # Cambia con il percorso della tua cartella

# Esegui la funzione
rename_images_in_folder(folder)
