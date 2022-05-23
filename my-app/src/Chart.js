import React, { useCallback, useState } from "react";
import { Container, Button } from "react-bootstrap";
import Tree from 'react-d3-tree';
import { Prompt } from 'react-router-dom'


const renderForeignObjectNode = ({nodeDatum}) => (
    <foreignObject width={300} height={250} x={-150}>
        <Button className='treeNodeButtons'>
          <div>{nodeDatum.name}</div>
          {nodeDatum.image ?
            <img src={nodeDatum.image} alt="Logo"/> :
            <div></div>
          }
        </Button>
    </foreignObject>
)

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
            renderCustomNodeElement={(rd3tProps) => 
                renderForeignObjectNode({...rd3tProps})
            }
            />
        </div>
        </Container>
    )
}

export default TreeGraph;