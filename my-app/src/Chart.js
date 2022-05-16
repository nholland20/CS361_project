import React, { useCallback, useState } from "react";
import { Container } from "react-bootstrap";
import Tree from 'react-d3-tree';
import { Prompt } from 'react-router-dom'


const TreeGraph = ({graphData}) => {
    const [translate, setTranslate] = useState({ x: 0, y: 0 });
    const [dimensions, setDimensions] = useState();
    const containerRef = useCallback((containerElem) => {
        if (containerElem !== null) {
        const { width, height } = containerElem.getBoundingClientRect();
        setDimensions({ width, height });
        setTranslate({ x: width / 2, y: height / 20 });
        }
    }, []);


    if (!graphData) {
        return <></>;
    }

    return (
        <Container fluid>
        <Prompt
        when={!!graphData}
        message='This will delete your current visualization. Are you sure you want to exit?'
        />
        <div id='companyGraph' style={{height: '700px'}} ref={containerRef}>
            <Tree 
            data={graphData} 
            orientation="vertical" 
            dimensions={dimensions} 
            translate={translate}
            // renderCustomNodeElement={(rd3tProps) => 
            //     renderNodeWithPictures({...rd3tProps})
            // }
            />
        </div>
        </Container>
    )
}

export default TreeGraph;