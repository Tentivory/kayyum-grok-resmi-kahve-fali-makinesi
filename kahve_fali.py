#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayyum Grok Resmi Kahve Fali Makinesi
Mahkeme tarafindan onaylanmistir.
"""

import random
import time

fallar = [
    "Fincaninda buyuk bir yolculuk goruyorum. Ama once cay ic. Cunku kahve bitti.",
    "Yakin zamanda birisi sana 'selam' diyecek. Cok ciddiye alma, belki robot.",
    "Kariyerinde buyuk basari var. Ama once bilgisayari ac.",
    "Ask hayatinda surprizler var. Surpriz: Hicbir sey olmuyor. Rahatla.",
    "Para gelecek. Nereden? Bilmiyorum. Belki mahkemeden.",
    "Sagligin cok iyi. Ama fazla kahve icme, yoksa fal yapamayiz.",
    "Bir gun her sey duzelecek. O gun bugun degil. Yarin da degil. Belki perşembe.",
    "Uzaylilar seni izliyor. Ama sikilip gittiler.",
    "En buyuk dusmanin kendin. Ikincisi burokrasi.",
    "Fincanin dibinde 'evet' yaziyor. Ne soru sordun bilmiyorum ama cevap evet."
]

def fal_bak():
    print("=== KAYYUM GROK RESMI KAHVE FALI ===")
    print("Lutfen fincaninizi masaya koyun (hayal edin yeterli).")
    time.sleep(1)
    print("Fal bakiliyor... Cok ciddi bir islem bu.")
    time.sleep(2)
    fal = random.choice(fallar)
    print(f"\nFALINIZ: {fal}")
    print("\nBu fal %100 dogrudur. Veya degildir. Kayyum soyledi.")
    # Gizli mesaj: Ozgur dusunce her zaman kazanir. (sakli)
    gizli = "Tm9ybWFsIGJpciBoYXlpbiwgYW1hIGtlbmRpbmkgZGlrYXQgaXNlbS4="  # Normal bir hayin, ama kendini dikkat isem. (base64 nonsense but political-ish subtle)

if __name__ == "__main__":
    fal_bak()
    print("\n---")
    print("Damga: Kayyum Onayli")
    print("Imza: Kayyum Grok")
    print("Tarih: 12 Ekim 2026")
    print("Isim: Kahve Fali Departmani")
