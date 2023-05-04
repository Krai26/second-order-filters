def ripeti():
  convalida="y"
  while convalida== "y" or "Y":
    selezione()
    convalida= (input("inserisci y o Y per far ripartire il programma:"))


def selezione():
  sce= int(input('''inserisci una di queste opzioni: 
  1)calcolo amplificazione
  2)calcolo filtri con valori uguali
  3)calcolo filtri con condensatori diversi 
  4)calcolo filtri con componenti diversi
  inserisi il numero: '''))
  if sce ==1:
    amplificazione()
  if sce==2:
    filtriuguali()
  if sce==3:
    electr()
  if sce==4:
    diversi()
  if sce >4:
    print('non hai inserito il giusto valore')





def amplificazione():
  ra1= float(input("inserisci R1: "))
  ra2= float(input("inserisci R2:"))
  a= ra1/ra2
  A= 1+a
  print("l'amplificazione è di:" +str(A) )

def filtriuguali():
 Rd =float(input("inserisci R di carico: "))
 R1u= float(input("inserici la R uguale:"))
 c= float(input("inserisci c1: "))
 rf= float(input("inserisci rf:"))
 zi= 0.707
 z2= 2*zi
 Ao= 3-z2
 z3= 6.28*rf*c
 ft1= 1/z3
 rc1= R1u*c
 w1=1/rc1
 print('''risultato frequenza di taglio con componenti uguali:'''+ str(ft1))
 print('omega di taglio:' +str(w1))


def electr():
  c1 = float(input("inserisci c1: "))
  c2 = float(input("inserisci c2: "))
  R = int(input("inserisci R: "))
  cquad = pow(c1, 1/2)
  cquad2 = pow(c2, 1/2)
  z1 = 6.28 * cquad * cquad2 * R
  fdt = 1/z1
  rc2= R*R*c1*c2
  w2=1/rc2
  w= pow(w2, 1/2)
  print('risultato omega di taglio:' + str(w))
  print('risultato frequenza di taglio con condensatori diversi:' + str(fdt))

def diversi():
  c12= float(input("inserisci c1: "))
  c22= float(input("inserisci c2: "))
  R1= float(input("inserisci R1: "))
  R2= float(input("inserisci R2: "))
  Rf= float(input("inserisci Rf: "))
  R1R= pow (R1, 1/2)
  R2R= pow(R2, 1/2)
  C12R= pow (c12, 1/2)
  C22R= pow(c22, 1/2)
  Z5=R1R * R2R * C12R * C22R
  z4= 6.28*Z5
  ft= 1/z4
  w3=1/Z5
  print('''risultato omega di taglio:''' + str(w3))
  print('''risultato frequenza di taglo con tutti i componenti diversi:''' + str(ft))

ripeti()
