#!/bin/bash
# Kullanım: ./kok-build-rapor.sh [çıkış_kodu]   (build.log gerekir)
cd "$(dirname "$0")"
LOG=build.log; OUT=kok-build-rapor.txt; KOD=${1:-?}
[ -f "$LOG" ] || { echo "build.log bulunamadı. Önce: sudo lb build"; exit 1; }
{
echo "KÖK OS DERLEME RAPORU  ($(date '+%F %T'))"
echo "lb çıkış kodu : $KOD   (0 = başarılı)"
echo "live-build    : $(dpkg -s live-build 2>/dev/null | grep ^Version)"
echo "Derleyen OS   : $(grep PRETTY_NAME /etc/os-release | cut -d= -f2)"
echo "Boş disk      : $(df -h . | tail -1 | awk '{print $4}')"
echo "ISO oluştu mu : $(ls *.iso 2>/dev/null || echo HAYIR)"
echo
echo "=== 1) ADIM İŞARETÇİLERİ (hangi hook çalıştı / bitti / hata verdi) ==="
grep -E '\[KOK(-HATA|-UYARI)?:' "$LOG" | sed 's/^/  /'
echo
echo "=== 2) İLK ÖLÜMCÜL HATA (E: / Error / failed) ve çevresi ==="
N=$(grep -nE '^E: |^Error|: command not found|returned a non-zero|Failed to|FAILED' "$LOG" | head -1 | cut -d: -f1)
if [ -n "$N" ]; then
  S=$((N>25?N-25:1)); sed -n "${S},$((N+15))p" "$LOG" | sed 's/^/  /'
else
  echo "  (belirgin hata satırı bulunamadı)"
fi
echo
echo "=== 3) Hata benzeri tüm satırlar (ilk 60) ==="
grep -nE '^E: |^W: .*(Failed|Unable)|Unable to locate package|has no installation candidate|404|Temporary failure' "$LOG" | head -60 | sed 's/^/  /'
echo
echo "=== 4) build.log son 60 satır ==="
tail -n 60 "$LOG" | sed 's/^/  /'
echo
echo "=== 5) Tanı ipucu ==="
grep -q 'Unable to locate package' "$LOG" && echo "  -> Bir paket adı Debian trixie'de yok: paket listelerini (config/package-lists/) kontrol et."
for A in A2 A3 A4 A5 A6 A7 A8 A9 A10 A11 A12; do grep -q "KOK-HATA:$A:" "$LOG" && echo "  -> Adım ${A#A} hook hatası (KOK-HATA:$A)."; done
grep -c 'KOK-UYARI' "$LOG" | sed 's/^/  -> Toplam uyarı sayısı: /'
grep -qE 'Temporary failure|Could not resolve' "$LOG" && echo "  -> İnternet/DNS sorunu."
grep -qE 'No space left' "$LOG" && echo "  -> Disk doldu."
} > "$OUT"
echo "Rapor hazır: $OUT  -> içeriğini geliştiriciye gönderin."
