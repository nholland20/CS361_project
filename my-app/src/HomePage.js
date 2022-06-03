import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import {Row, Col, Card, Button, Container} from "react-bootstrap"
import { useNavigate } from "react-router-dom";

const HomePage = (props) => {
    const navigate = useNavigate();
    return (
        <>
        <Container fluid>
            <Row className="justify-content-md-center">
                <Col xs lg="2">
                    <h1>Who Owns Who?</h1>
                </Col>
            </Row>
            <Row className="justify-content-md-center">
                <Col lg="6">
                    <h3>Select one of the options below to discover who owns who in the corporate world.</h3>
                </Col>
            </Row>
        </Container>
        <Container fluid>
            <Row xs={1} md={2} className="g-4">
                <Col>
                <Card border="primary">
                    <Card.Body>
                        <Card.Title>By Company</Card.Title>
                        <Card.Text>Click 'Start' to type in the company that you want to see the heirarchy for.</Card.Text>
                        <Button variant="primary" onClick={() => navigate("/by-company")}>Start</Button>
                    </Card.Body>
                </Card>
                </Col>
                <Col>
                <Card border="primary" >
                    <Card.Body>
                        <Card.Title>By Industry</Card.Title>
                        <Card.Text>Click 'Choose Company' to view the heirarchy of a company from a specific industry.</Card.Text>
                        <Button variant="primary" onClick={() => navigate("/by-industry")}>Choose Company</Button>
                    </Card.Body>
                </Card>
                </Col>
            </Row>
        </Container>
        </>
    )
}

export default HomePage;