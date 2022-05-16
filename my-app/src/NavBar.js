import {Navbar, Container, Nav} from "react-bootstrap"
import { NavLink } from 'react-router-dom';

const SiteNavbar = (props) => {
    return (
        <Navbar bg="dark" variant="dark">
            <Container>
                <Nav className="me-auto">
                    <NavLink to={'/'} style={{color: '#ffffff', marginRight: '15px'}}>
                        <div>Home</div>
                    </NavLink>
                    <NavLink to={'/by-company'} style={{color: '#ffffff', marginRight: '15px'}}>
                        <div>By Company</div>
                    </NavLink>
                    <NavLink to={'/by-industry'} style={{color: '#ffffff', marginRight: '15px'}}>
                        <div>By Industry</div>
                    </NavLink>
                </Nav>
            </Container> 
        </Navbar>
    )
}

export default SiteNavbar