import {Navbar, Container, Nav} from "react-bootstrap"

const SiteNavbar = (props) => {
    const { onNavSelect } = props
    return (
        <Navbar bg="dark" variant="dark">
            <Container>
                <Nav className="me-auto" onSelect={onNavSelect}>
                    <Nav.Link href="#home" eventKey={"home"}>Home</Nav.Link>
                    <Nav.Link href="#by-company" eventKey={"by-company"}>By Company</Nav.Link>
                    {/* <Nav.Link href="#by-industry" eventKey={"by-industry"}>By Industry</Nav.Link> */}
                </Nav>
            </Container> 
        </Navbar>
    )
}

export default SiteNavbar