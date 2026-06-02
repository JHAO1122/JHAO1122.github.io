function RawBlock(el)
  if el.format:match("html") then
    if el.text:match("polyfill%.io") then
      return {} -- 返回空，直接抹杀这一行
    end
  end
  return el
end

function Script(el)
  if el.src:match("polyfill%.io") then
    return {} -- 针对新版 pandoc 节点的拦截
  end
  return el
end