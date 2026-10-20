import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python msys2run.py dosya.msys2 [argümanlar]")
        sys.exit(1)

    yol = sys.argv[1]
    if not yol.endswith(".msys2"):
        print("Uyarı: dosya uzantısı .msys2 değil, yine de çalıştırılıyor.")

    try:
        with open(yol, encoding="utf-8") as f:
            satirlar = f.read().splitlines()
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {yol}")
        sys.exit(1)

    if satirlar and satirlar[0].startswith("#!"):
        satirlar = satirlar[1:]

    kod = "\n".join(satirlar)
    sonuc = subprocess.run(["bash", "-c", kod, yol] + sys.argv[2:])
    sys.exit(sonuc.returncode)

main()
