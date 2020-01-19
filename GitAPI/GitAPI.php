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
    // 
    // Create New User`s Directory Flow
    // 1. newUserDirectory($userId)
    //
    // Create New File(Project) Flow
    // 1. initGit($userId, $userEmail, $fileId)
    //
    // File Save Flow
    // 1. save a real file
    // 2. commitFile($userId, $fileId, $timeStamp)
    // 
    // Restore File Flow
    // 1. restoreFile($userId, $fileId, $timeStamp)
    //
    // Get Branch List Flow
    // 1. getCheckPointList($userId, $fileId)
    //
    ////////////////////////////////////////////////////////////////////////////
    $path = "/www/cineditor/cineditor/tests/test/";

    // new user
    function newUserDirectory($userId){
        global $path;
        $cmd = "mkdir $path$userId";
        $result = system($cmd);
        return $result;
    }

    // init git
    function initGit($userId, $userEmail, $fileId){
        global $path;
        $cmd = "mkdir $path$userId/$fileId";
        $result = system($cmd);
        $cmd = "cd $path$userId/$fileId ; git init";
        $result1 = system($cmd);
        $cmd = "cd $path$userId/$fileId ; git config --local user.name '$userId'";
        $result2 = system($cmd);
        $cmd = "cd $path$userId/$fileId ; git config --local user.email $userEmail";
        $result3 = system($cmd);
        return "$result\n$result1\n$result2\n$result3\n";
    }

    // commit file(call this function after save a real file)
    function commitFile($userId, $fileId, $timeStamp){
        global $path;
        $cmd = "cd $path$userId/$fileId ; git add *";
        $result = system($cmd);
        $cmd = "cd $path$userId/$fileId ; git commit -m 'commit $timeStamp'";
        $result1 = system($cmd);
        $cmd = "cd $path$userId/$fileId ; git branch -b $timeStamp";
        $result2 = system($cmd);
        return "$result\n$result1\n$result2\n";
    }

    // restore file
    function restoreFile($userId, $fileId, $timeStamp){
        global $path;
        $cmd = "cd $path$userId/$fileId ; git checkout $timeStamp";
        $result = system($cmd);
        return $result;
    }

    // get branch list
    function getCheckPointList($userId, $fileId){
        global $path;
        $cmd = "cd $path$userId/$fileId ; git branch";
        $result = system($cmd);
        return $result;
    }

?>