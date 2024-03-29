FTTranslate: A translation tool experiment for Google Fusion Tables

Alpha software!

Installation::

  git clone git@github.com:trey0/fttranslate.git
  cd fttranslate
  cp local_settings_template.py local_settings.py
  # put your fusion tables username/password and your api key for google
  # translate into local_settings.py
  python test.py

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

Use Cases for FT Translator / FT-翻訳家のユースケース

At the location of disaster, local groups are creating maps highlighting important locations/entities. The maps are based on fusion tables consisting of geographical data (cities, prefectures, street names) and building names (hospitals, train stations, shops etc.), in local language. 

I) International rescue teams have arrived in the affected area, and would like to use these community-generated maps to aid their efforts. However in order to do this, they need to understand the content shown in the maps.

II) The data contained within the maps would need to be crowdsourced to different locations, where volunteers or people acting on that data do not understand the original language. They would need a translated version fo the data for consumption.

User

1) Opens the map; it is visible in the local language

2) Has an affordance available to view the map in a different language, and chooses a language of his choice

3) Sees the map content in a language he understands



