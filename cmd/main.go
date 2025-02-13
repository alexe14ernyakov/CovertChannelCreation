package main

import (
	"flag"
	"fmt"

	server "covertchannel/lab1/internal/server"
)

func main() {
	intruderIp := flag.String("intruder", "localhost", "IP-address of intruder")
	intruderPort := flag.String("port", "1337", "Port of intruder")

	flag.Parse()

	address := *intruderIp + *intruderPort

	serv := server.New(address)
	serv.Start()

	fmt.Println("Hello World")
}
