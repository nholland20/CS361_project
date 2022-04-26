import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import {Row, Col, Card, Button} from "react-bootstrap"

const HomePage = (props) => {
    const {handleNavSelect} = props;
    return (
        <>
        <Row>
            <h1>Who Owns Who?</h1>
        </Row>
        <Row>
            <h3>Select one of the options below to discover which who owns who in the corporate world.</h3>
        </Row>
        <Row md={3} xs={2} className="g-4">
            <Col>
            <Card border="primary" style={{width: "18rem"}}>
                <Card.Body>
                    <Card.Title>By Company</Card.Title>
                    <Card.Text>Click 'Start' to type in the company that you want to see the heirarchy for.</Card.Text>
                    <Button variant="primary" onClick={() => handleNavSelect("by-company")}>Start</Button>
                </Card.Body>
            </Card>
            </Col>
            {/* <Col>
            <Card border="primary" style={{width: "18rem"}}>
                <Card.Body>
                    <Card.Title>By Industry</Card.Title>
                    <Card.Text>Click 'Choose Company' to view the heirarchy of a company from a specific industry.</Card.Text>
                    <Button variant="primary" onClick={() => handleNavSelect("by-industry")}>Choose Company</Button>
                </Card.Body>
            </Card>
            </Col> */}
        </Row>
        </>
        
    )
}

export default HomePage;