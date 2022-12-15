#1. Loo PS skript, mis muudab emailis olevad nimed korralikeks nimedeks

#Mirko kohava

#13.12.2022

cls
$loop = 1
while($loop -eq 1){                                 #alustab loopi

$kysimus = (Read-Host = "mis on CSV faili nimi?: ")               #kusib kasutajalt mis on faili nimi kust see votab emailid
                   
if ($kysimus -notmatch ".csv$") {                             #vaatab kas file on .csv fail

       Write-Host "file pole .csv fail!"                        #karjub kasutaja peale kui ei ole csv fail
}
else {

$loop = 0                                             #lopetab loopi kui kasutaja sai oige faili sisse kirjutatud

$skriptiAsukoht = $MyInvocation.MyCommand.Path
$dir = Split-Path $skriptiAsukoht                                           #impordib selle faili mis kasutaja on sisse kirjutadud ja hakkab kasutama seda
$emailid = get-content -path $dir\$kysimus


    foreach($email in $emailid) {  
                                                                #runnib seda kasku iga rea peal kuni pole enam

    $test = $email.Replace('@gmail.com','').replace('.',' ')        #eemaldab emaili märgid et saada puhast nime
    $test = (Get-Culture).TextInfo.ToTitleCase($test)               #muudab vaiksed tahed suureks                          

    $test >> $dir\korrastatud.txt                                      #viskab tulemuse teksti faili
       
    
        
        }
    }
}
