import { QueryClient, QueryClientProvider } from "react-query";
import { ThemeProvider } from "styled-components";
import { GlobalStyle } from "./styles/global-style";
import { ReactQueryDevtools } from "react-query/devtools";
import { theme, lightTheme } from "./styles/theme";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Search from "./pages/Search";
import { useRecoilValue } from "recoil";
import { isDarkAtom } from "./atom/atoms";

const queryClient = new QueryClient();

function App() {
  const isDark = useRecoilValue(isDarkAtom);
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={isDark ? theme : lightTheme}>
        <GlobalStyle />
        <Router>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/search" element={<Search />} />
          </Routes>
        </Router>
        <ReactQueryDevtools initialIsOpen={true} />
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
