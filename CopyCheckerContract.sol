pragma solidity >=0.4.22 <0.6.0;

contract CopyChecker{
    
    address constant private contractOwner = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c;
    
    struct CheckPoint{
        uint256 time;
        bytes32 fileHash;
    }
    
    struct File{
        uint256 fileId;
        uint256 owner;
        bool isDeleted;
        mapping(uint256 => CheckPoint) history;
        uint256 historySize;
    }
    
    mapping(uint256 => File) files;
    uint256[] fileIds;
    
    function createFile(uint256 userId, bytes32 fileHash) public returns(uint256){
        assert(msg.sender == contractOwner);
        
        File memory tempFile;
        uint256 tempTime = now;
        
        tempFile.fileId = uint256(keccak256(abi.encodePacked(bytes32(userId), fileHash, bytes32(tempTime))));
        tempFile.owner = userId;
        tempFile.isDeleted = false;
        tempFile.historySize = 0;
        
        CheckPoint memory tempCheckPoint;
        tempCheckPoint.time = tempTime;
        tempCheckPoint.fileHash = fileHash;
        
        files[tempFile.fileId]=tempFile;
        fileIds.push(tempFile.fileId);
        
        files[tempFile.fileId].history[files[tempFile.fileId].historySize++] = tempCheckPoint;
        return tempFile.fileId;
    }
    
    function updateFile(uint256 fileId, bytes32 fileHash) public{
        assert(msg.sender == contractOwner);
        
        assert(isFileInFiles(fileId));
        
        CheckPoint memory tempCheckPoint;
        tempCheckPoint.time = now;
        tempCheckPoint.fileHash = fileHash;
        
        files[fileId].history[files[fileId].historySize] = tempCheckPoint;
    }
    
    function getContractOwner() public pure returns(address){
        return contractOwner;
    }
    
    function getNumberOfFiles() public view returns(uint256){
        return fileIds.length;
    }
    
    function deleteFile(uint256 fileId) public{
        assert(msg.sender == contractOwner);
        assert(isFileInFiles(fileId));
        
        files[fileId].isDeleted = true;
    }
    
    function isFileInFiles(uint256 fileId) private view returns(bool){
        for(uint256 i = 0; i < fileIds.length ; i++){
            if(fileIds[i] == fileId) return true;
        }
        return false;
    }
    
    function destroyContract() public{
        assert(msg.sender == contractOwner);
        
        selfdestruct(msg.sender);
    }
    
}
