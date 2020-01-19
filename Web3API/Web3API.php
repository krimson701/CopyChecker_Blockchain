#!/usr/bin/php
<?php
    ////////////////////////////////////////////////////////////////////////////
    //
    // file path example : /www/cineditor/cineditor/tests/test/$userId/$fileId/fileId.txt
    //
    // $path : File storage path
    // $userId : User ID
    // $userEmail : User Email
    // $fileId : File ID
    // $timeStamp : yyyymmddhhmmss (14 characters)
    // $fileHash : Hash of file (32 Bytes)
    //
    // Add fileHash to Chain
    // 1. createFile($userId, $fileHash)
    //
    // Update fileHash from Chain
    // 1. updateFile($fileId, $fileHash)
    //
    // Delete fileHash from Chain
    // 1. deleteFile($fileId)
    //
    ////////////////////////////////////////////////////////////////////////////
    $path = "/www/cineditor/cineditor/tests/";
    $prog = "use_contract.py"
    // Add fileHash
    function createFile($userId, $fileHash){
        global $path;
        $cmd = "python3 $path$prog 0 0 $userId $fileHash";
        $result = system($cmd);
        return $result;
    }
    // Update FileHash 
    function updateFile($fileId, $fileHash){
        global $path;
        $cmd = "python3 $path$prog 1 $fileId 0 $fileHash";
        $result = system($cmd);
        return $result;
    }
    // Delete fileHash
    function deleteFile($fileId){
        global $path;
        $cmd = "python3 $path$prog 2 $fileId 0 0";
        $result = system($cmd);
    }
    return $result;
?>
