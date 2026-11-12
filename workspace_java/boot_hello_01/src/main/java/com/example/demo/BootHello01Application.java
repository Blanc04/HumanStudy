package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class BootHello01Application {

	public static void main(String[] args) {
		System.out.println("Hello World");
		SpringApplication.run(BootHello01Application.class, args);
	}

}
