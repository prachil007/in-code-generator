package com.yourcompany.yourappname.controllers;

import java.util.List;

import javax.validation.Valid;
import javax.websocket.server.PathParam;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.yourcompany.yourappname.models.AuthenticatedUser;
import com.yourcompany.yourappname.models.##table_name_cs##;
import com.yourcompany.yourappname.services.##table_name_cs##Service;

@RestController
@RequestMapping("/yourapipath/##table_name_plural##")
public class ##table_name_cs##Controller extends BaseController {

	@Autowired
	private ##table_name_cs##Service ##table_name_lcs##Service;

	@GetMapping(value = "/list", produces = MediaType.APPLICATION_JSON_UTF8_VALUE)
	public List<##table_name_cs##> getAll##table_name_cs_plural##()
	{
		return ##table_name_lcs##Service.findAll##table_name_cs_plural##();
	}
	
	@GetMapping(value = "/{##id_field_lcs##}", produces = MediaType.APPLICATION_JSON_UTF8_VALUE)
	public ##table_name_cs## get##table_name_cs##(@PathParam("##id_field_lcs##") Long ##table_name_lcs##Id)
	{
		return ##table_name_lcs##Service.findBy##table_name_cs##Id(##table_name_lcs##Id);
	}

	@PostMapping(consumes = MediaType.APPLICATION_JSON_UTF8_VALUE, produces = MediaType.APPLICATION_JSON_UTF8_VALUE)
	public ##table_name_cs## add##table_name_cs##(@RequestBody @Valid ##table_name_cs## ##table_name_lcs##)
	{
		AuthenticatedUser authenticatedUser = getAuthenticatedUser();
		##table_name_lcs##Service.add##table_name_cs##(##table_name_lcs##, authenticatedUser.getId());
		return ##table_name_lcs##Service.findBy##table_name_cs##Id(##table_name_lcs##.get##id_field_cs##());
	}

	@PutMapping(consumes = MediaType.APPLICATION_JSON_UTF8_VALUE, produces = MediaType.APPLICATION_JSON_UTF8_VALUE)
	public ##table_name_cs## update##table_name_cs##(@RequestBody @Valid ##table_name_cs## ##table_name_lcs##)
	{
		AuthenticatedUser authenticatedUser = getAuthenticatedUser();
		##table_name_lcs##Service.update##table_name_cs##(##table_name_lcs##, authenticatedUser.getId());
		return ##table_name_lcs##Service.findBy##table_name_cs##Id(##table_name_lcs##.get##id_field_cs##());
	}
	
	@DeleteMapping(consumes = MediaType.APPLICATION_JSON_UTF8_VALUE, produces = MediaType.APPLICATION_JSON_UTF8_VALUE)
	public ResponseEntity<Object> delete##table_name_cs##(@RequestBody @Valid ##table_name_cs## ##table_name_lcs##)
	{
		AuthenticatedUser authenticatedUser = getAuthenticatedUser();
		##table_name_lcs##Service.update##table_name_cs##(##table_name_lcs##, authenticatedUser.getId());
		return new ResponseEntity<Object>(HttpStatus.NO_CONTENT);
	}
}
