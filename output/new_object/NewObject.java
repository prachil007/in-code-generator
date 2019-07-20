package com.yourcompany.yourappname.models;

import com.yourcompany.yourappname.common.models.BaseModel;
import com.fasterxml.jackson.annotation.JsonFormat;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

public class NewObject extends BaseModel {

    private static final long serialVersionUID = 776435080244520932L;

	private Long newObjectId;
	private String name;
	private String addressLineField1;
	private String addressLineField2;
}
