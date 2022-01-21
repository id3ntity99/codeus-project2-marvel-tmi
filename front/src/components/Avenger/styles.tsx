import styled from "styled-components";
import { motion } from "framer-motion";

export const PostZone = styled(motion.div)`
  position: relative;
  z-index: 0;
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

export const PopUpWrapper = styled(motion.div)`
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  background-color: rgba(0, 0, 0, 0.7);
`;

export const PopUp = styled(motion.div)`
  width: 40%;
  height: auto;
  background-color: ${props => props.theme.bgColor.lighter};
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 1)),
    url(https://mblogthumb-phinf.pstatic.net/MjAxNzExMjBfMjY3/MDAxNTExMTY4MTk3MjA4.9qSmwAvE_7v49pwbHMOz6_4JYB7r89YOPudsCa5t2W0g.Q9jhzhBnJ3VCPcwACUMLmkK3gcUHx4yC4EcIw0GSi_wg.PNG.citymedia1/2017-11-20_17%3B46%3B35.PNG?type=w800);
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  overflow: hidden;
`;

export const PopupHeader = styled.header`
  background-color: #eb2324;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 50px;
  padding: 10px;
`;

export const Title = styled.h3`
  font-weight: 900;
`;

export const CancelBtn = styled.div`
  background-color: ${props => props.theme.bgColor.default};
  border-radius: 50%;
  width: 35px;
  height: 35px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
`;

export const PopUpInfo = styled.article`
  padding: 10px 20px;
  & > div {
    &:first-child {
      margin-top: 20px;
    }
    margin-bottom: 30px;
    display: grid;
    grid-template-columns: 1fr 2fr;
    h5 {
      font-weight: 600;
    }
    p {
      font-size: 0.8rem;
      a {
        color: #eb2324;
      }
    }
  }
`;
