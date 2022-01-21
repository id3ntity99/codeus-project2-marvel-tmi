import styled from "styled-components";
import { motion } from "framer-motion";

export const HeaderWrapper = styled.header`
  position: fixed;
  z-index: 1;
  width: 100%;
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 50px;
  background-color: ${props => props.theme.bgColor.lighter};
`;

export const MainLogo = styled(motion.svg)``;

export const Search = styled.div`
  position: relative;
  svg {
    cursor: pointer;
    position: absolute;
    right: 0;
  }
`;

export const SearchInput = styled(motion.input)`
  transform-origin: center right;
`;
