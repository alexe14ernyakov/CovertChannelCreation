package server

type Server struct {
	address string
}

func New(address string) *Server {
	return &Server{
		address: address,
	}
}
