import React from "react";
import { Button, Form} from "react-bootstrap";


const ByCompanyPage = ({handleCompanyChange, message}) => {

    return (
        <>
        <h1>By Company</h1>
        <p>Please type the name of the company whose organizational structure you would like to view</p>
        <Form onSubmit={handleCompanyChange}>
            <Form.Group className="mb-3">
                <Form.Label htmlFor="inputCompany">Company Name Here:</Form.Label>
                <Form.Control as="textarea" id="inputCompany" name="inputCompany" rows={1}></Form.Control>
            </Form.Group>
            <Button type="submit">Submit</Button>
        </Form>
        {message != null && 
        <p>
            {message}
        </p>
        }
        </>
    )
}

export default ByCompanyPage;