



#1. Loo PS skript, mis muudab emailis olevad nimed korralikeks nimedeks

#Mirko kohava

#13.12.2022




cls
$kysimus = (Read-Host = "mis on CSV faili nimi?: ")                                            #kusib kasutajalt mis on faili nimi kust see votab emailid

$skriptiAsukoht = $MyInvocation.MyCommand.Path
$dir = Split-Path $skriptiAsukoht
$emailid = Get-Content -path $dir\emails.csv                                                   #impordib selle faili mis kasutaja on sisse kirjutadud ja hakkab kasutama seda


If (Test-Path -Path $kysimus) {                                                                #testib kas fail on arvutis olemas
       
    foreach($email in $emailid) {  
                                                                #runnib seda kasku iga rea peal kuni pole enam

    $test = $email.Replace('@gmail.com','').replace('.',' ')
    $test = (Get-Culture).TextInfo.ToTitleCase($test)               #muudab vaiksed tahed suureks
    $test                              

    $test >> $dir\korrastatud.txt                                      #viskab tulemuse teksti faili

    } } Else {

    Write-Output "$kysimus ei ole olemas"                                                      #kui faili pole arvutis siis tuleb see ette
    


    }


