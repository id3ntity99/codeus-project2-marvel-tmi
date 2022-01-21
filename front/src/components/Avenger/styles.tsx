import styled from "styled-components";
import { motion } from "framer-motion";

export const PostZone = styled.div`
  width: 250px;
  height: 300px;
  border-radius: 7px;
`;

export const Post = styled(motion.div)`
  width: 250px;
  height: 300px;
  border-radius: 7px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: ${props => props.theme.bgColor.lighter};
  cursor: pointer;
`;

export const Name = styled.h3`
  font-weight: 800;
  margin-bottom: 10px;
`;

export const Description = styled.p`
  font-size: 0.9rem;
  opacity: 0.8;
`;

export const Info = styled.div`
  border-top: 1px solid ${props => props.theme.bgColor.default};
  display: flex;
  justify-content: space-between;
  padding: 10px;
  font-size: 0.7rem;
  opacity: 0.8;
`;

export const PopUpWrapper = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export const PopUp = styled(motion.div)`
  width: 300px;
  height: 300px;
  background-color: white;
`;
