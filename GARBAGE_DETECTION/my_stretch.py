# -*- coding: utf-8 -*-
"""my_stretch.py

Original file is located at
    https://colab.research.google.com/drive/1TIAKXMsqI8lYQXpypVxmjZhyI_z3uChq
"""

import numpy as np                        # Importa Numpy
import skimage.io as io                   # Importa il modulo Input/ouput di SK-Image
from skimage.transform import resize      # Importa il modulo resize da SK-Image
from os import listdir                    # Importa il modulo listdir da OS

"""Alcuni valori vengono calcolati più e più volte, per riutilizzare i valori calcolati secondo necessità ottimizzando l'esecuzione, implementiamo il modulo lru_cache di functools. Essa consente alla funzione di memorizzare valori già calcolati e di riutilizzarli quando necessario."""

from functools import lru_cache           # Importa il modulo lru_cache da functools

"""Stretchiamo le immagini per ottenere immagini quadrate della stessa grandezza per poterci lavorare in maniera più intuitiva"""

@lru_cache(maxsize=None)          # Dimensione della cache (default:128, con None non diamo un limite ma consumiamo molte risorse --> Colab)
def f_stretched(initial_batch, final_batch, dataset_path, dimension, f_type):
  ''' 
    Stretcha un'immagine a dimensione quadrata e la carica in un ndarray (utilizza lru_cache)
      # PRECONDIZIONE: immagini divise in batch
      # POSTCONDIZIONE: restituisce un array di immagini stretchate secondo una dimensione quadrata scelta dall'utente

    ----------
    PARAMETRI:
      initial batch: batch da cui partire
          int
      final_batch: batch finale
          int
      dataset_path: indirizzo dei batch del dataset
          string ('/content/drive/MyDrive/Project/DataSet/batch_')
      dimension: dimensione dell'immagine quadrata in uscita
          int
      f_type: scelta se la funzione deve essere utilizzata per immagini (0) o per immagini segmentate (1)
          int

    ----------
    RETURN:
      numpy.ndarray
          4D-array (number_img x dimension x dimension X channel)
  ''' 
  list_img_stretched = list()     # Crea una lista vuota per le immagini stretchate

  for i in range(initial_batch, final_batch):
    num = str(i+1)                 # Casting
    if f_type == 1:
      # listdir: restituisce un elenco contenente i nomi delle voci nella directory data dal path.
      for fname in sorted(listdir(dataset_path + num + '/segmentation')):                               

        img = np.float32(io.imread(dataset_path + num + '/segmentation/' + fname))/255           # Legge e normalizza le immagini segmentate

        img_stretched = resize(img, (dimension, dimension), order=0)                # Stretcha le immagini in formato 512x512 con interpolazione Nearest-Neighbour

        # Porta l'immagine stretchata da 3D a 1D (come vuole la rete in input)
        img_stretchedbn = to_one_dimension(img_stretched)

        # Aggiunge un elemento alla fine dell'elenco
        list_img_stretched.append(img_stretchedbn)

    elif f_type == 0:
      # listdir: restituisce un elenco contenente i nomi delle voci nella directory data dal path.
      for fname in sorted(listdir(dataset_path + num)):                               
        if fname != 'segmentation': 
          img = np.float32(io.imread(dataset_path + num + '/' + fname))/255           # Legge e normalizza le immagini
          img_stretched = resize(img, (dimension, dimension), order=0)                # Stretcha le immagini in formato 512x512 con interpolazione Nearest-Neighbour

          list_img_stretched.append(img_stretched)                                    # Aggiunge un elemento alla fine dell'elenco

    else:
      print("ERRORE F_TYPE ERRATO")
      break

    npa_stretched = np.array(list_img_stretched)                                  # Crea un array di tutte le immagini stretchate

  return npa_stretched

def array_on_file(filename, array):
  ''' 
      Salva un array su un file binario
        # PRECONDIZIONE: array caricato
        # POSTCONDIZIONE: restituisce un file caricato con gli elementi dell'array

      ----------
      PARAMETRI:
        filename: nome del file
            string ("filename.ext")
        array:
            numpy.ndarray
  ''' 
  with open(filename, 'wb') as f:             # wb = write binary                                   
    np.save(f, array)
  f.close()

def array_from_file(filename):
  ''' 
      Legge un array da un file binario
        # PRECONDIZIONE: array salvato in un file binario
        # POSTCONDIZIONE: restituisce un array

      ----------
      PARAMETRI:
        filename: nome del file
            string ("filename.ext")

    ----------
    RETURN:
      numpy.ndarray
  ''' 
  with open(filename, 'rb') as f:             # rb = read binary  
    array = np.load(f)
  return array

def to_one_dimension(img):
  ''' 
      estrae il bitplane meno significativo (dove c'è l'informazione della mask binaria della segmentazione) del canale R 
      (è indifferente quale tra RGB tanto ogni bitplane 0 contiene la stessa informazione)
      per alte informazioni vedi: bitplane_test.ipynb
        # PRECONDIZIONE: array 3D (meglio se ancora non stretchato)

      ----------
      PARAMETRI:
        img: array di una immagine RGB
            array [N x N x 3]

    ----------
    RETURN: array di una immagine binaria
            array [N x N x 1]
  ''' 
  
  return (img[ : , : , 0])%2
