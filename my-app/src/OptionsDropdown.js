import React from "react";
import { Container, Form } from "react-bootstrap";

const OptionsDropdown = ({optionsList, handleOptionSelect}) => {
    if (!optionsList) {
        return <></>;
    }

    return (
        <Container>
            <div>
                More clarification needed. Please choose from the following list and select the company name as it appears on Wikipedia.
            </div>
            <Form.Group className="mb-3">
                <Form.Label>Company Name</Form.Label>
                <Form.Select name='inputCompany' onChange={handleOptionSelect}>
                    <option>Company Name</option>
                    {optionsList.map(co =>
                        <option id={co} key={co} className="companyNames" value={co}>{co}</option>)}
                </Form.Select>
            </Form.Group>
        </Container>
    )
}

export default OptionsDropdown;