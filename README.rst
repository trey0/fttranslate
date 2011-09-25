FTTranslate: A translation tool experiment for Google Fusion Tables

Requirements:
FT == Fusion Table

1) Given:
     a source FT, Sft, and a source column, Scol, within it which is of FT type text string,
     and each row of which contains human-readable place names in source human language, Slang, 
   translate each source row string into target human language, Tlang, and place the resulting
   string into the corresponding row of target FT, Tft, target column, Tcol.

2) The translation mechanism is done using the human language translation service TranService(Slang,Tlang)


