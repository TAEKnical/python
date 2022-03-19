import wave
import binascii

with open("morse.wav","rb")as f:
	dot="27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80"
	dot=dot.replace(" ","")
	blank="80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80"
	blank=blank.replace(" ","")
	wav_header="52 49 46 46 A3 BB 00 00 57 41 56 45 66 6D 74 20 10 00 00 00 01 00 01 00 40 1F 00 00 40 1F 00 00 01 00 08 00 64 61 74 61 7F BB 00 00"
	wav_header=wav_header.replace(" ","")

	morse_text=f.read()
	morse_text=binascii.hexlify(morse_text)
	morse_text=morse_text.decode()
	morse_text=morse_text.upper()
	morse_text=morse_text.replace(dot,".")
	morse_text=morse_text.replace(blank," ")
	# morse_text=morse_text.replace("...","-")
	# morse_text=morse_text.replace("   ","blank")
	# morse_text=morse_text.replace(" ","")
	# morse_text=morse_text.replace("blank"," ")
	morse_text=morse_text.replace(wav_header,"")
	f.close()
with open("morse.txt","w") as w:
	w.write(morse_text)
	w.close()
print(morse_text)
print("모스부호가 morse.txt 파일로 저장되었습니다. https://morsecode.scphillips.com/translator.html에서 해독하세요.")
