# Zoo 1-st stage

print('I love animals!')
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")

# Zoo 2-nd stage

camel = r"""
The camel habitat...
 ___.-''''-.
/___ @     |
',,,,.     |       _.'''''''._
     '     |     /             \
     |     \ _.-'               \
     |                           '.-' '-.
     |                                   ',
     |                                     '',
     ',,-,                                 ':;
          ',,| ;,,                       ,' ;;
             ! ;  !'',,,',',,,,'!       ;   ;:
            : ;    ! !      ! !  ;     ;    :;
             ; ;    ! !     ! !   ;   ;     ;,
            ; ;     ! !    ! !     ; ;
            ; ;     ! !   ! !       ; ;
           ;,,       !,!  !,!       ;,;
           /_I       L_I  L_I       /_I
Look at that!"""

# Zoo 3-rd stage

lion = r"""
The lion habitat...
                                               ,w.
                                             ,YWMMw ,M ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW" @\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
 "^MP__.-'   ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \ :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
The lion is roaring!"""

deer = r""" 
The deer habitat... 
    /| |\
 `__\\ //__'
    || ||
 \__`\ |'__/
  `_\\ //_'
 _.,:---;,._
 \_:     :_/
   |@. .@|
   |     |
   ,\.-./ \
   ;;`-'   `---__________-----.-.
   ;;;                         \_\
   ';;;                         |
    ;    |                      ;
     \    \    \        |      /
      \_,  \   /        \     |\
        |'; |  |,,,,,,,,/ \   \ \_
        |   |  |           \  /   |
         \  \  |           | / \  |
          | || |           | |  | |
          | || |           | |  | | 
          | || |           | |  | |
          | || |           | |  | |
          |_||_|           |_|  |_|
Pretty good! """

goose = r""" 
The goose habitat... 
                              _
                         ,- "" "".
                       , '   ____  `.
                     , ' ,'      `. `._
  (`.     _..--.._ ,'  ,'          \   \
 (`-.\  .-""     ""'  /            ( d _b
(`._ ` -"" ,._        (             `-(  \
<_ `     ( <`<        \                `-._\
 <`-      (__< <       :
  (__      (_<_<       ;
    `------------------------------------------               
Beautiful! """

bat = r""" 
The bat habitat... 
_____________            _____________
~-.           \ |\___/| /          .-~ 
  ~-.         \ / o o \ /       .-~ 
      >        \\  W  //        < 
     /          /~---~\         \ 
    /_         |        |       _\ 
      ~-.      |        |    .-~ 
         ;      \      /     i 
        /___    /\    /\    ___\ 
           ~-. /  \_/   \ .-~ 
              V           V 
It's doing fine. """

rabbit = r""" 
The rabbit habitat... 
           , 
          /|     __ 
         / |   ,-~ / 
        Y :|  // / 
       | jj /( .^ 
       >-"~"-v" 
       /        Y 
      jo o      | 
     ( ~T~     j 
      >._-'  _./ 
     /  "~"    | 
    Y      _,  | 
  /|  ;-"~ _   l 
/ l/  ,-"~      \ 
\//\/         .- \ 
 Y         /      Y 
 l         I      ! 
 ]\         _\   /"\ 
(" ~----( ~   Y.    ) 
It looks fine! """

# Zoo 4-th stage

print("Please enter the number of the habitat you would like to view\n(camel = 1, lion = 2, deer = 3, goose = 4, bat = 5,  rabbit = 6):")
while True:
    name = input("Виберіть номер, або напишіть exit: ")
    if name == '1':
        print(camel)
    elif name == '2':
        print(lion)
    elif name == '3':
        print(deer)
    elif name == '4':
        print(goose)
    elif name == '5':
        print(bat)
    elif name == '6':
        print(rabbit)
    elif name == 'exit':
        print("See you later!")
        break
    else:
        print("Error, спробуйте ще раз")
