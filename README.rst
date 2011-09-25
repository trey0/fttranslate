FTTranslate: A translation tool experiment for Google Fusion Tables

Alpha software!

Quick resources and developer tips:

 * Live app is at http://ft-translate.appspot.com/

 * GitHub project page is https://github.com/trey0/fttranslate

 * Git sample::

     # initial checkout
     git clone git@github.com:trey0/fttranslate.git
     cd fttranslate
     
     # pulling somebody else's update
     git pull origin master
     
     # pushing your changes
     git add changedfile.txt
     git commit -m 'made changes'
     git push origin master

Requirements:
FT == Fusion Table

1) Given:
     a source FT, Sft, and a source column, Scol, within it which is of FT type text string,
     and each row of which contains human-readable place names in source human language, Slang, 
   translate each source row string into target human language, Tlang, and place the resulting
   string into the corresponding row of target FT, Tft, target column, Tcol.

2) The translation mechanism is done using the human language translation service TranService(Slang,Tlang)

3) In the initial version, we will writeback the translated text into a fusion table. This fusion table will then be used to visualize the map in the new language.


User-Interface

1) There will be an affordance for the user at the map visualization level to specify the language s/he wants to view the map in.
2) There will be another affordance to initiate the translation process.


