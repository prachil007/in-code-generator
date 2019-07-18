package com.yourcompany.yourappname.models;

import com.mobisoftinfotech.common.models.BaseModel;
import com.fasterxml.jackson.annotation.JsonFormat;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

public class NewObject extends BaseModel {

    private static final long serialVersionUID = 407030274640050931L;

	private Long newObjectId;
	private String name;
	private String addressLineField1;
	private String addressLineField2;
	private String cityI;
}
