import { motion } from "framer-motion";
import styled from "styled-components";

export const ToggleButton = styled.div`
  background-color: ${props => props.theme.bgColor.default};
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  width: 50px;
  height: 28px;
  border-radius: 15px;
`;

export const Light = styled.svg`
  position: absolute;
  top: 6px;
  left: 7px;
`;

export const Dark = styled.svg`
  position: absolute;
  top: 6px;
  right: 4px;
`;

export const ModeZone = styled.div`
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const Circle = styled(motion.div)`
  position: absolute;
  z-index: 10;
  top: center;
  left: 0;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  border: 1px solid black;
  background-color: white;
  cursor: pointer;
`;
