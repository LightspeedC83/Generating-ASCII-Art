# Generating ASCII Art
this program uses a reference image to generate ascii art
works best with reference images that are about 150-250 pixels wide and don't feature a lot of colors

# Example Output:

                .'":;;;;;;;;;::;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:,'.             
            .^iiiiiiiiiiiiiii!iiiiiii!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii".          
           .!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii!'         
          .!iiiiiiiiiiii}X)[[[}{{)fiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii!iiiii!.        
          `iiiiiiiiiiiiirXX(.   .+)iiiiiiiiiiiiii!iiiiiiiiiiiiiiiiii!lI;;;Iliiiiiiiiiiiiiii^        
          `iiiiiiiiiiii-v('.   ../~!iiiiiiiiiiiiii!iiiiiiiiiiI"'..            ..';iiiiiiiii".       
          `iiiiiiiiii)X~.   .,f,^x!iiiiiiiiiiiiiiiiiiiiil"..   ..`,I!iiiiiiil;^..  .^!iiiii".       
          ^iiiiiiiiirX!....+zXXXv1!iiiiiiiiiiiiiiiii!,..  .':!iiiiiiiiiiiiiiiiiii!^. .'!iii"        
          `iiiiiiii!zX{'`/)''?f{iiii!iiiii!iiiiii!^.. .';iiiiiiiiiiiiiiiiiiiiiiiiiii;. .`ii^        
          `iiiiii+vrYXXci.  .>|iiiiiiiiiiiiiii!^.  .^!iiiii!iiiiiiiiiiiiiiiiiiiiiii!ii". .l"        
          `iiiii[Xz`^}'.  .'{(iiiiiiiiiiiiii;.  .^!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiI.  .        
          `iiiii/X|.    ."r}iiiiiiiiiiiii!^.  'IiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiI.          
          `iiii!nX<.....}\!iiiiiiiiiiiil'. ."iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii,.         
          `iiii~XXrjjfft/friiiiiiiiiil.. .;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'         
          `iiiii_]]]]]]]]iiiiiiiiiil.. .Iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;.        
          `iiiii!iiiiiiiiiiiiiiii!'. .Iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii!.        
          `iiiiiiiiiiiiiiii!iiii^. .:iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii^        
          `iiiiiiiiiiiiiiiiiii;. .^iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii^        
          `iiiiiiiiiiiiiiiii!'  '!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii,        
          `iiiiiiiiiiiiiiii:. .:iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii,        
          `iiiiiii!iiiiii!'..'iiiiiiiiiiiiiii!iiiiiiii!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"        
          `iiiiiiii!iiiiI. .:iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`        
          ^iiiiiiiiiiii". .liiiiiiiiiiiii!iiiiiii~nXt{{1)((|||\\/ttfjX<iiiiiiiiiiiiiiiiiiii.        
          `iiiiiiiiiii'  `iiiiiiiiiiiiiiii!iiii+zXXXXx`.           .~z!iiiiiiiiiiiiiiiiiiiI.        
          `iiiiiiiii!. ."ii!iiiiiiiiiiiiiiiiiiii\XXXXXX{.          .//iiiiiiiiiiiiiiiiii!i"         
          `iiiiiiiil. .;iiiiiiiiiiiiiiiiii!iiiiii>uXzX?'.          'X?iiiiiiiiiiiiiiiiiiii.         
          `iiiiiiiI. .liiiiiiiiiiiiiiiiiiii!iiii]zXu;.            .+ciiiiiiiiiiiiiiiiiiii:.         
          `iiiiii;. .liiiiiiiiiiiiiiiiiiiiiiii/XX)'.             ..//iiiiiiiiiiiiiiiiiiii'          
          `iiiii;. .liiiiiiiiiiiiiiiiiiiii!+vXzi.          .'-i. .`X?iiiiiiiiiiiiiiiiiii:.          
          `iiiiI. .liiiiiiiiiiiiiiiiiiiii~cXX{.          .^fXXXn^'~z!iiiiiiiiiiiiiiiiii!.           
          `iiil. .liiiiiiiiiiiiiiiiiiiii?XXX).        ..>zzXXzXXX)//iiiiiiiiiiiiiiiiiii^  ,^        
          `ii!. .;iiiiiiiiiiiiiiiiiiiiiivXXX~.      .'(X1:vvvXXXXXx>ii!iiiiiiiiiiiiiii:. 'i^        
          `ii' .,iiiiiiiiiiiiiiiiiiiiii>XXXX/'.   .;uc!. .'|u]XX)iiiiiiiiiiiiiiiiiiiil. .li^        
          `i". ^iiiiiiiiiiiiiiiiiiiiiii!xXXXX|'..]Xt`.     'v)iiiiiiiiiiiiiiiiiiiiiii. .:ii^.       
          `I  .iiiiiiiiiiiiiiiiiiiii~uXf_XXXXXzxz_.        .j\iiiiiiiiiiiiiiiiiiiiii`..,iii^.       
          .. .;iiiiiiiiiiiiiiiiiii-cXX:-X(XXXXx,.         .iX+iii!iiiiiiiiiiiiiiiii^ .^iiii^        
             ^iiiiiiiiiiiiiiiiiiifXXXx..'tXX{'.         ..]X-iiiiiiiiiiiiiiiiiiiii^..`iiiii^        
            .!iiiiiiiiiiiiiiiiiiizXXX[.   ..          .'[X\!iiiiiiiiiiiiiiiiiiiii^..`iiiiii^        
           ."iiiiiiiiiiiiiiiiiii-XXXX;.             .^jz]i!iiiiiiiiiiiiiiiiiiiii` .`iiiiiii^        
           .!iiiiiiiiiiiiiiiiiii)XzXn'.          ..<zx<!iiiiiii!iiiiiiiiiiiiiii' .^iiiiiiii^        
           ^iiiiiiiiiiiiiiiiii!ijXXX}.          '|X)iiiiiiiiiiiiiiiiiiiiiiiii!. ."iiiii!iii^        
          .;iiiiiiiiiiiiiiiiiiiiXXXX;           .-X}iiiiiiiiiiiiiiiiiiiiiiiil. .:iiiiiiiiii^        
          .iiiiiiiiiiiiiiiiiiii?XXXn'............'`tv~iiiiiiiiiiiiiiiiiiiii,. .liiiiiiiiiii^        
          `iiiiiiiiiiiiiiiiiiii|XXXXXXXXXXXXXXXXXXXXX\i!iiiiiiiiiiiiiiiiii` .'!iiiiiiii!iii^        
          "iiiiiiiiiiiiiiiiiiii/XXXXXXXXXXXXXXXXXXz}!!!iiiiiiiiiiiii!iiiI. ."!iiiiiiiiiiiii^.       
         .,iiiiiiiiiiiiiiiiiii!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii^  .liiiiiiiiiiiiiii^.       
         .:iiii!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiI. .^iiiiiiiiiiiiiiiii^        
         .:iiii!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii!iiiiiiiiiiiiiiiiiii`  .liiiiiiiiiiiiiiiiii^        
          ,iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii". .,iiiiiiiiiiiiiiiiiiii^        
          `iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;. .`iiiiiiiiiiiiiiiiiiiiii^        
          .!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;. .'!iiiiiiiiiiiiiiiiiiiiiii^        
           :iii!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;. .'lii!iiiiiiiiiiiiiiiiiiiiii^        
           .!iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii,. .'liiiiiiiiiii}Xn,^^^^",/_iiii^        
            ^iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii!`. .`!iiiiiiii!iiii<vXn"   .'u!iiii^.       
             "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:.. .,iiii!iiiiiiiiii?c)'.    .>|iiiii^.       
          ''  `iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;.  .'lii!iiiiiiiiiiii{X?'.  .,xx^(_iiiii^        
          `i". .Iiiiiiiiiiiiiiiiiiiiii!iiiiiiii:.. ..:iiiiiiiiiiiii!!ii{X\. .._xuXXXjiiiiii^        
          `iil.  .;iiiiiiiiiiiiiiiii!!iiiii;`.  ..;iiiiiiiiiiiiiii!iii!{XX!`t1..'x>!iiiiiii^        
          `iiiiI.. .':!iiiiiiiiiiiiii!I"..   .^liiiiiiiiiiiiiiiiiiii+vt/XXc!.  .`niiiiiiiii^.       
          `iiiiiii:..   ..'`^^^`....  ....,!iiiiiiiiiiiiiiiiiiiiiii!vX_.^'.  .'{/i!iiiiiiii^.       
          `iiiiiiiiiii;^'..........`,Iiiiiiiiiiiiiiiiiiiiiiiiiiiiii+XX`    .,x}!iiiiiiiiiii^        
         .'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii1Xt'....'/[iiiiiiiiiiiii`        
          .,iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiijXXXXXXXXXc~iiiiiiiiiii:.        
           .^iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii!i!iiiiii!!iiiiiiiiiii;.    
             .`Iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii_~!   
                  ...................................................................
