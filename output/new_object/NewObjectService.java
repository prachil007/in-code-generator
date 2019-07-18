package com.yourcompany.yourappname.services;

import javax.validation.Valid;
import org.springframework.validation.annotation.Validated;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import javax.validation.constraints.NotNull;
import org.springframework.transaction.annotation.Transactional;
import com.yourcompany.yourappname.daos.NewObjectDao;
import com.yourcompany.yourappname.models.NewObject;
import com.mobisoftinfotech.common.models.BaseModel;

@Service
@Validated
public class NewObjectService {
 
    @Autowired
    private NewObjectDao newObjectDao;
    
    @Transactional(rollbackFor = Exception.class)
    public NewObject findByNewObjectId
        (@NotNull(message = "required.newObjectId") Long newObjectId) {
        return newObjectDao.findByNewObjectId(newObjectId);
    }
    
    @Validated
    @Transactional(rollbackFor = Exception.class)
    public int addNewObject(
        @Valid NewObject newObject,
        @NotNull(message = "required.loggedInUserId") Long loggedInUserId) {
        newObject.updateCCUU(loggedInUserId);
        return newObjectDao.addNewObject(newObject);
    }
    
    @Validated
    @Transactional(rollbackFor = Exception.class)
    public int updateNewObject(
        @Valid NewObject newObject,
        @NotNull(message = "required.loggedInUserId") Long loggedInUserId) {
        newObject.updateUU(loggedInUserId);
        return newObjectDao.updateNewObject(newObject);
    }
    
    @Transactional(rollbackFor = Exception.class)
    public int deleteNewObjectByNewObjectId(
        @NotNull(message = "required.newObjectId") @Param("newObjectId") Long newObjectId,
        @NotNull(message = "required.loggedInUserId") Long loggedInUserId) {

        BaseModel baseModel = new BaseModel();
        baseModel.updateUU(loggedInUserId);
        return newObjectDao.deleteNewObjectByNewObjectId(newObjectId, baseModel);
    }
}
